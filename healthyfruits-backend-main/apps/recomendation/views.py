from .models import *
from .serializers import RecomendationSerializers, ListAPISerializers
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
import numpy as np
import pandas as pd
from rest_framework.pagination import PageNumberPagination
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from apps.food.models import Meal 

# Create your views here.
class ListViewRecomendatios(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Meal.objects.all()
    serializer_class = ListAPISerializers
    pagination_class = PageNumberPagination
    filter_fields = ['id']

class View_Recomendation_API(CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = RecomendationModel.objects.all()
    serializer_class = RecomendationSerializers
    
    def post(self, request, *args, **kwargs):
        
        ratings = pd.read_csv("../healthyfruits-backend/users.csv",engine="python", sep=',', quotechar='"', error_bad_lines=False)
        foods = pd.read_csv("../healthyfruits-backend/foods.csv",engine="python", sep=',', quotechar='"', error_bad_lines=False)
           
        user_freq = ratings[['user_id', 'recipe_id']].groupby('user_id').count().reset_index()
        user_freq.columns = ['user_id', 'n_ratings']
        
        mean_rating = ratings.groupby('recipe_id')[['rating']].mean()
        lowest_rated = mean_rating['rating'].idxmin()
        foods.loc[foods['recipe_id'] == lowest_rated]
        highest_rated = mean_rating['rating'].idxmax()
        foods.loc[foods['recipe_id'] == highest_rated]
        ratings[ratings['recipe_id']==highest_rated]
        ratings[ratings['recipe_id']==lowest_rated]
        
        foods_stats = ratings.groupby('recipe_id')[['rating']].agg(['count', 'mean'])
        foods_stats.columns = foods_stats.columns.droplevel()
        
        def create_matrix(df):
            
            N = len(df['user_id'].unique())
            M = len(df['recipe_id'].unique())
            
            user_mapper = dict(zip(np.unique(df["user_id"]), list(range(N))))
            food_mapper = dict(zip(np.unique(df["recipe_id"]), list(range(M))))
            
            user_inv_mapper = dict(zip(list(range(N)), np.unique(df["user_id"])))
            food_inv_mapper = dict(zip(list(range(M)), np.unique(df["recipe_id"])))
            
            user_index = [user_mapper[i] for i in df['user_id']]
            movie_index = [food_mapper[i] for i in df['recipe_id']]
        
            X = csr_matrix((df["rating"], (movie_index, user_index)), shape=(M, N))
            
            return X, user_mapper, food_mapper, user_inv_mapper, food_inv_mapper
        
        X, user_mapper, food_mapper, user_inv_mapper, food_inv_mapper = create_matrix(ratings)      

        def find_similar_foods(foods_id, X, k, metric='cosine', show_distance=False):
            
            neighbour_ids = []
            
            food_ind = food_mapper[foods_id]
            food_vec = X[food_ind]
            k+=1
            kNN = NearestNeighbors(n_neighbors=k, algorithm="brute", metric=metric)
            kNN.fit(X)
            food_vec = food_vec.reshape(1,-1)
            neighbour = kNN.kneighbors(food_vec, return_distance=show_distance)
            for i in range(0,k):
                n = neighbour.item(i)
                neighbour_ids.append(food_inv_mapper[n])
            neighbour_ids.pop(0)
            return neighbour_ids
        
        
        foods_titles = dict(zip(foods['recipe_id'], foods['recipe_name']))
        foods_images = dict(zip(foods['recipe_id'], foods['image_url']))
        foods_ingredients = dict(zip(foods['recipe_id'], foods['ingredients']))
        foods_nutrients = dict(zip(foods['recipe_id'], foods['nutritions']))
        
        id = request.data['id_recipe']
        foods_id = int(id)
        
        similar_ids = find_similar_foods(foods_id, X, k=10,metric="euclidean")
        fo_title = foods_titles[foods_id]
        fo_image = foods_images[foods_id]       
        
        #make json type array begin
        response_data = []
        final_response = {}

        #print(f"Since you watched {fo_title}")  
        for i in similar_ids:
            try:
                response_record = {}
                response_record['name_food'] = foods_titles[i]
                response_record['image_url'] = foods_images[i]
                response_record['ingredientes'] = foods_ingredients[i]
                response_record['nutritions'] = foods_nutrients[i]
                response_data.append(response_record)
                
            except:
                print("")  
    
        request.data._mutable = True
        request.data['recomendation_food'] = str(response_data)
        request.data._mutable = False
        serializer = RecomendationSerializers(data = request.data)
    
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
         
        
        
                
        
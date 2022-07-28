<template lang="html">
  <div >
    
    <h1>{{ msg }}</h1>
    <p>
      For a guide and recipes on how to configure / customize this project,<br />
      check out the
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener"
        >vue-cli documentation</a
      >.
    </p>
    <b-alert show>Default Alert</b-alert>
    <b-alert variant="success" show>Success Alert</b-alert>
    <div>
      <b-button @click="closeNav" class="float-center mt-5">
        <b-icon icon="x-circle"></b-icon>
      </b-button>
    </div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="css">
</style>

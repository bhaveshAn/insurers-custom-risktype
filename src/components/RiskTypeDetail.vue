<template>
  <div class="risk_type_detail">
    <div class="container">
    <h1>Risk Type: {{risk_type_name}}</h1>
    </div>
    <ul class="list-group">
      <li class="list-group-item" v-for="field in fields"><b>{{field.name}}:</b> <em>{{field.type}}</em></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'RiskTypeDetail',
  data () {
    return {
      fields: [],
      risk_type_name: 'None',
    }
  },
  methods:{
  greet: function(greeting){
      alert(greeting);
  },
  presskey: function(){
      console.log('Pressed');
  },
  hitEnter: function(){
      console.log('You Hit Enter');
  }
  },
  created: function(){
    this.$http.get('http://localhost:5000/v1/risk_type/'+this.$route.params.id)
	.then(function(response) {
            console.log("Created");
            this.fields = response.data.fields
            this.risk_type_name = response.data.risk_type.name
	    console.log(response.data.risk_type.name)
	})
	.catch((err) => {
	    console.log(err)
	})
      }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

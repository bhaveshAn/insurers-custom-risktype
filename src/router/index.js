import Vue from 'vue'
import Router from 'vue-router'
import Resource from 'vue-resource'
import RiskTypeDetail from '@/components/RiskTypeDetail'

Vue.use(Router)
Vue.use(Resource)

export default new Router({
  routes: [
     {
      path: '/:id',
      name: 'RiskTypeDetail',
      component: RiskTypeDetail
    }
  ]
})

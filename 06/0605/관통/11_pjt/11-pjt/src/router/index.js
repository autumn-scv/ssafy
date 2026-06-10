import TableView from '@/views/TableView.vue'
import ThreeDGraphView from '@/views/ThreeDGraphView.vue'
import TwoDGraphView from '@/views/TwoDGraphView.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/table',
      name:'table',
      component: TableView
    },
    {
      path:'/2d',
      name:'2d',
      component: TwoDGraphView
    },
    {
      path:'/3d',
      name:'3d',
      component: ThreeDGraphView
    }
  ],
})

export default router

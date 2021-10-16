import Vue from 'vue';
import VueRouter from 'vue-router';
import TilePad from './views/TilePad.vue';
import About from './views/About.vue';
import Settings from './views/Settings.vue';

Vue.use(VueRouter);

export default new VueRouter({
	mode: 'history',
	routes: [
		{
			path: '/layout/:layout',
			name: 'tilePadWithRoute',
			component: TilePad,
			props: true
		},
		{
			path: '/',
			name: 'tilePad',
			component: TilePad
		},
		{
			path: '/about',
			name: 'about',
			component: About
		},
		{
			path: '/settings',
			name: 'settings',
			component: Settings
		}
	]
});

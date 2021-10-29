import Vue from 'vue';
import App from './App.vue';
import store from './store/store';
import router from './router';
import vuetify from './plugins/vuetify';
import './registerServiceWorker';
import i18n from './i18n';
import VueClipboard from 'vue-clipboard2'; 


Vue.use(VueClipboard);
Vue.config.productionTip = false;

const app = new Vue({
	store,
	router,
	vuetify,
	i18n,
	render: h => h(App)
});

app.$mount('#app');

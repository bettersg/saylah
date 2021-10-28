import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import 'material-design-icons-iconfont/dist/material-design-icons.css'; // Ensure you are using css-loader

Vue.use(Vuetify);

export default new Vuetify({
	icons: {
		iconfont: 'md'
	},
	theme: {
		themes: {
			light: {
				primary: '#2196f3',
				secondary: '#b0bec5',
				accent: '#ffffff',
				error: '#b71c1c'
			},
			dark: {
				accent: '#000000'
				//here you will define primary secondary stuff for dark theme
			}
		},
		dark: true
	}
});

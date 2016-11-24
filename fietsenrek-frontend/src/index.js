import angular from 'angular';

import {techsModule} from './app/techs/index';
import 'angular-ui-router';
import routesConfig from './routes';

import {main} from './app/main';
import {title} from './app/title';
import {footer} from './app/footer';

import './index.css';

angular
  .module('app', [techsModule, 'ui.router'])
  .config(routesConfig)
  .component('app', main)
  .component('fountainTitle', title)
  .component('fountainFooter', footer);

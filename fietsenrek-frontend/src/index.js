import angular from 'angular';

import 'angular-ui-router';
import routesConfig from './routes';

import {main} from './app/main';
import {title} from './app/title';
import {racks} from './app/racks';
import {footer} from './app/footer';

import './index.css';

angular
  .module('app', ['ui.router', 'ngMaterial'])
  .config(routesConfig)
  .component('app', main)
  .component('fountainTitle', title)
  .component('fountainRacks', racks)
  .component('fountainFooter', footer);

import angular from 'angular';

import 'angular-ui-router';
import 'satellizer';
import routesConfig from './routes';
import socialConfig from './social';

import {main} from './app/main';
import {auth} from './app/auth';
import {title} from './app/title';
import {racks} from './app/racks';
import {footer} from './app/footer';

import './index.css';

angular
  .module('app', ['ui.router', 'ngMaterial', 'satellizer'])
  .config(routesConfig)
  .config(socialConfig)
  .component('app', main)
  .component('fountainAuth', auth)
  .component('fountainTitle', title)
  .component('fountainRacks', racks)
  .component('fountainFooter', footer);

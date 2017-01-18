export const auth = {
  template: require('./auth.html'),
  controller($scope, $auth, $log, $http, $mdDialog, $mdToast) {
    $scope.user = {};

    $scope.login = function () {
      $auth.login($scope.user)
        .then(() => {
          $scope.user.password = "";
          $mdDialog.hide();
        })
        .catch(err => {
          const messages = angular.fromJson(err.data);
          for (const key in messages) {
            if (messages.hasOwnProperty(key)) {
              $scope.showMessage(`${key}: ${messages[key][0]}`);
            }
          }
        });
    };

    $scope.signup = function () {
      $auth.signup($scope.user)
        .then(() => {
          $mdDialog.hide();
          $scope.showMessage("Your account has been created. Now you can log in.");
        })
        .catch(err => {
          const messages = angular.fromJson(err.data);
          for (const key in messages) {
            if (messages.hasOwnProperty(key)) {
              $scope.showMessage(`${key}: ${messages[key][0]}`);
            }
          }
        });
    };

    /* social login (at this moment only Facebook) */
    $scope.authenticate = function (provider) {
      $auth.authenticate(provider)
        .then(response => {
          $scope.user = angular.fromJson(response.data.user);
          $mdDialog.hide();
        })
        .catch(err => {
          $log.log(err);
        });
    };

    $scope.logout = function () {
      $auth.logout().then(() => {
        $http({
          method: 'POST',
          url: 'http://localhost:8000/rest-auth/logout/'
        });
      });
    };

    $scope.isAuthenticated = function () {
      return $auth.isAuthenticated();
    };

    /* to display login modal */
    $scope.showLoginContainer = function (ev) {
      $mdDialog.show({
        controller: DialogController,
        contentElement: '#loginDialog',
        targetEvent: ev,
        clickOutsideToClose: true
      });
    };

    /* to display flash messages */
    $scope.showMessage = function (text) {
      $mdToast.show($mdToast.simple()
        .textContent(text)
        .position('top right')
      );
    };

    function DialogController($scope, $mdDialog) {
      $scope.hide = function () {
        $mdDialog.hide();
      };

      $scope.cancel = function () {
        $mdDialog.cancel();
      };
    }
  }
};

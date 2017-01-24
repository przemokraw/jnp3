/* eslint-disable */

export const racks = {
  template: require('./racks.html'),
  controller($http, $log, $window, $location, $mdToast, $auth) {
    this.path = $location.path();

    // get racks
    $http({
      method: 'GET',
      url: 'http://localhost:9999/racks/list/'
    }).then(response => {
      this.racks = angular.fromJson(response.data);
      $log.log(this.racks);
      $log.log(new Map(this.racks));
    }, response => {
      $log.log(response);
    });

    // get problems
    $http({
      method: 'GET',
      url: 'http://localhost:9999/racks/problems/'
    }).then(response => {
      this.problems = angular.fromJson(response.data);
      this.problemsMap = new Map(this.problems);
      $log.log(this.problemsMap);
    }, response => {
      $log.log(response);
    });

    // upvote
    this.upvote = function (rackId) {
      for (let i = 0; i < this.racks.length; i++) {
        if (this.racks[i].id === rackId) {
          this.racks[i].vote++;
          break;
        }
      }

      $http({
        method: 'PATCH',
        url: 'http://localhost:9999/racks/'.concat(rackId).concat('/upvote/')
      }).then(response => {
        $log.log(response);
      }, response => {
        $log.log(response);
      });
    };

    // downvote
    this.downvote = function (rackId) {
      for (let i = 0; i < this.racks.length; i++) {
        if (this.racks[i].id === rackId) {
          this.racks[i].vote--;
          break;
        }
      }

      $http({
        method: 'PATCH',
        url: 'http://localhost:9999/racks/'.concat(rackId).concat('/downvote/')
      }).then(response => {
        $log.log(response);
      }, response => {
        $log.log(response);
      });
    };

    // solve
    this.solve = function (rackId) {
      for (let i = 0; i < this.racks.length; i++) {
        if (this.racks[i].id === rackId) {
          this.racks[i].solved = true;
          break;
        }
      }

      $http({
        method: 'PATCH',
        url: 'http://localhost:9999/racks/'.concat(rackId).concat('/solve/')
      }).then(response => {
        $log.log(response);
      }, response => {
        $log.log(response);
      });
    };

    // create
    this.isCreating = false;
    this.create = function () {
      this.isCreating = true;
      $location.hash('addHidden');
      $anchorScroll();
    };

    this.save = function () {
      this.newData = {};
      this.newData.place_id = 42; //random value, not used but needed
      this.newData.city = this.newCity;
      this.newData.country = this.newCountry;
      this.newData.description = this.newDescription;
      this.newData.problem = this.newProblem;
      this.newData.solved = false;
      $http({
        method: 'POST',
        url: 'http://localhost:9999/racks/create/',
        data: this.newData
      }).then(response => {
        this.newRack = angular.fromJson(response.data);
        this.racks.push(this.newRack);
        this.isCreating = false;
        $location.hash('addHidden');
      },response => {
        $mdToast.show($mdToast.simple()
          .textContent("Incorrect values or server error, try again.")
          .position("bottom left")
          .parent(document.querySelectorAll('#addHidden'))
        );
        $log.log(response);
      });
    };

    this.cancel = function () {
      this.isCreating = false;
      $location.hash('racks');
    };

    // sorting
    this.sortingFactor = -1;
    this.sortingOrderVerbose = "descending";
    this.sort = function () {
      this.sortingFactor *= -1;
      this.sortingOrderVerbose = this.sortingFactor === -1 ? "descending" : "ascending";
      this.racks.sort((first, second) => {
        if (first.vote !== second.vote) {
          return this.sortingFactor * (first.vote - second.vote);
        }
        return this.sortingFactor * first.city.localeCompare(second.city);
      });
    };

    // searching
    this.searchText = "";
    this.onSearch = function (event) {
      $log.log(event.keyCode);
      if (event.keyCode !== 13) {
        return;
      }
      $log.log(this.searchText);
      if (this.searchText === "") {
        $http({
          method: 'GET',
          url: 'http://localhost:9999/racks/list/'
        }).then(response => {
          this.racks = angular.fromJson(response.data);
        }, response => {
          $log.log(response);
        });
      } else {
        $http({
          method: 'GET',
          url: 'http://localhost:9999/racks/description-search?text='.concat(this.searchText)
        }).then(response => {
          this.racks = angular.fromJson(response.data);
        }, response => {
          $log.log(response);
        });
      }
    };

    this.isAuthenticated = function () {
      return $auth.isAuthenticated();
    };

    this.unsolvedImages = {};
    this.unsolvedImages["There are no racks"] = 'http://127.0.0.1/images/no_racks.jpg';
    this.unsolvedImages["There are too few racks"] = 'http://127.0.0.1/images/too_few_racks.jpg';
    this.unsolvedImages["The racks are not safe"] = 'http://127.0.0.1/images/unsafe_racks.jpg';

    this.solvedImage = 'http://127.0.0.1/images/solved.jpg';
  }
};

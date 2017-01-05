/* eslint-disable */

export const racks = {
  template: require('./racks.html'),
  controller($http, $log, $window, $location) {
    this.path = $location.path();
    $log.log(this.path);

    // get racks
    $http({
      method: 'GET',
      url: 'http://localhost:8000/racks/list/'
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
      url: 'http://localhost:8000/racks/problems/'
    }).then(response => {
      this.problems = angular.fromJson(response.data);
      this.problemsMap = new Map(this.problems);
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
        url: 'http://localhost:8000/racks/'.concat(rackId).concat('/upvote/')
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
        url: 'http://localhost:8000/racks/'.concat(rackId).concat('/downvote/')
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
        url: 'http://localhost:8000/racks/'.concat(rackId).concat('/solve/')
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
      $location.hash('add');
    };

    this.save = function () {
      this.newData = {};
      this.newData.place_id = 42;
      this.newData.city = this.newCity;
      this.newData.country = this.newCountry;
      this.newData.description = this.newDescription;
      this.newData.problem = this.newProblem;
      this.newData.solved = false;
      $http({
        method: 'POST',
        url: 'http://localhost:8000/racks/create/',
        data: this.newData
      }).then(response => {
        this.newRack = angular.fromJson(response.data);
        this.racks.push(this.newRack);
      }, response => {
        $log.log(response);
      });
      this.isCreating = false;
      $location.hash('addHidden');
    };

    this.cancel = function () {
      this.isCreating = false;
      $location.hash('addHidden');
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
    this.onSearchTextChanged = function () {
      $log.log(this.searchText);
    };
  }
};

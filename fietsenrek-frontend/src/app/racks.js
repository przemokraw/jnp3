export const racks = {
  template: require('./racks.html'),
  controller($http, $log) {
    $http({
      method: 'GET',
      url: 'http://localhost:8000/racks/list/'
    }).then(response => {
      $log.log(response);
      this.result = "Success";
    }, response => {
      $log.log(response);
      // We get error because backend doesn't let our frontend make requests
      // Responses miss header 'Access-Control-Allow-Origin' with walue '*'
      // Marta is working on that.
      // By now let's populate template with some example data
      this.racks = [{rackId: 1, rackPlace: "MIMUW"}, {rackId: 2, rackPlace: "Metro Wilanowska"}];
    });
  }
};

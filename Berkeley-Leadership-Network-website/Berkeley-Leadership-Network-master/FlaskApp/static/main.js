(function () {

  'use strict';

  angular.module('webApp', [])

  .controller('webAppController', ['$scope', '$log', '$http',
    function($scope, $log, $http) {
    console.log("Angular")

     // fire the API request
    $scope.data = [];

    $scope.cleanData = function(responseData) {
        var cleanedData = []
        for(var i = 0; i < responseData['Location'].length; i++) {
            cleanedData[i] = {}
            for(var key in responseData) {
                cleanedData[i][key] = responseData[key][i].replace(/\b\w/g, l => l.toUpperCase());
            }
            cleanedData[i]['First'] = cleanedData[i]['Full Name'].split(/\s(.+)/)[0];
        }
        console.log(cleanedData);
        return cleanedData;
    };

    $scope.search = function(searchLocation, searchIndustry, searchJob, searchStage) {
        return function (item) {
            if (searchLocation && !(item['Location'].toLowerCase().includes(searchLocation.toLowerCase()))) {
                return false;
            }
            if (searchIndustry && !(item['Investment interest/sector'].toLowerCase().includes(searchIndustry.toLowerCase()))) {
                return false;
            }
            if (searchJob && !(item['Primary Job Title'].toLowerCase().includes(searchJob.toLowerCase()))) {
                return false;
            }
            if (searchStage && !(item['Stage (Pre-Seed, Seed, Series A/B/C)'].toLowerCase().includes(searchStage.toLowerCase()))) {
                return false;
            }

            return true;
        }
    };

    $http.post('/dataRequest').
      success(function(results) {
        console.log(results);
        $scope.data = $scope.cleanData(results);
        console.log($scope.data);
      }).
      error(function(error) {
        console.log(error);
      });

  }

  ]);

}());

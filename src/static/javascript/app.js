(function(){
    "use strict";
    var app = angular.module('myapp', [ ]);

    app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    });

    app.controller('APPController', ['$scope','$http', '$window', function($scope,$http,$window){
        console.log('My app');
        $scope.email = '';
        $scope.group = [];
        $scope.generate_status = 'Generate Groups';
        $scope.isActive = false;

        $scope.generate = function(){
        	$http.get('/generate_list').then(function(data){
        		console.log(data);
                $scope.generate_status = 'Generated!';
                $scope.isActive = true;
        	});
        }

        $scope.find_group = function(){
        	console.log('email: ' + $scope.email);
        	$http.get('/find_group/' + $scope.email).then(function(response){
        		console.log(response);
        		$scope.group = response.data ;
        	});
        }

    }]);


})();
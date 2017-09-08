app
.config(['$interpolateProvider',function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
  }])
.controller('navbar-controller',['$scope',function($scope){
    $scope.message = 'Welcome to Django With Angular';
    $scope.home = function(){

        alert('Home Clicked............');
    };
}])
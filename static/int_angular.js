'use strict';
/* global angular */

var order = angular.module('order', ['ngCookies', 'ngResource']);

order.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

order.config(function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

order.config(function ($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
});

order.run(function ($rootScope, $log, $http, $cookies) {

    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];

});


order.factory('OrderService', function ($resource) {
    return $resource("/api/orders/:id/", null,
        {
            'patch': {method: 'PATCH'}
        })
});

order.controller("OrderListCtrl", function ($scope, OrderService) {
    $scope.orders = OrderService.query();
    $scope.complete = function (order) {
        order.complete = true;
        OrderService.patch({id: order.id}, order).$promise.then(function () {
            $scope.orders = OrderService.query();
            $scope.$emit('orders', 'updated');
        });
    };

});

order.factory('UserInfoService', function ($resource) {
    return $resource("/api/scores/")
});

order.controller("UserInfoCtrl", function ($scope, $location, UserInfoService) {
    $scope.scores = UserInfoService.query();
    $scope.$on('orders', function () {
        $scope.scores = UserInfoService.query();
    });
});

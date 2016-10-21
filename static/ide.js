var app = angular.module("ide");

app.controller("mainWindowController", ["$scope", "$timeout", function ($scpoe, $timeout) {
    $scope.ws;
    $scope.rows;
    $scope.currentPage;
    $scope.totalRows;
    $scope.maxSize;
    $scope.itemsPerPage;
    $scope.isConnected = false;
    $scope.uuid;

    $scope.init = function() {
        if ($scope.uuid) {
            $scope.ws = new WebSocket("ws://" + location.host + "/ws/" + $scope.uuid);
        } else {
            $scope.ws = new WebSocket("ws://" + location.host + "/ws/");
        }
        $scope.ws.binaryType = "arraybuffer";

        $scope.ws.onopen = function() {
            console.log("Connected.");
            $scope.$apply(function() {
                $scope.isConnected = true;
            });
        };

        $scope.ws.onclose = function() {
            console.log("Connection closed.");
            $scope.apply(function() {
                $scope.isConnected = false;
            });
        };

        $scope.ws.onerror = function(e) {
            console.log(e.msg);
        };
    }

    $timeout($scope.init, 1000);
}]);

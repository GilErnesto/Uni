// Declarar vmInstance globalmente
var vmInstance;

// ViewModel KnockOut
var vm = function () {
    console.log('ViewModel initiated...');
    var self = this;
    self.baseUri = ko.observable('http://192.168.160.58/Paris2024/api/Torch_route');
    self.displayName = 'Paris 2024 Torch Route';
    self.records = ko.observableArray([]);
    self.allRecords = ko.observableArray([]); // Para armazenar todos os dados da API

    //--- Page Events
    self.activate = function () {
        console.log('CALL: getRoutes...');
        var composedUri = self.baseUri();
        ajaxHelper(composedUri, 'GET').done(function (data) {
            console.log('Data received:', data);
            self.records(data); // Exibe os dados inicialmente
            self.allRecords(data); // Mantém uma cópia de todos os dados
        });
    };

    //--- start ....
    self.activate();
    console.log("VM initialized!");
};

// Função auxiliar para chamadas AJAX
function ajaxHelper(uri, method, data) {
    return $.ajax({
        type: method,
        url: uri,
        dataType: 'json',
        contentType: 'application/json',
        data: data ? JSON.stringify(data) : null,
        error: function (jqXHR, textStatus, errorThrown) {
            alert("AJAX Call[" + uri + "] Fail...");
        }
    });
}

// Inicialização do Knockout ViewModel
$(document).ready(function () {
    console.log("ready!");
    vmInstance = new vm();
    ko.applyBindings(vmInstance);

    // Adiciona eventos de clique aos elementos <area>
    $('area').on('click', function (event) {
        event.preventDefault();
        var zone = $(this).attr('alt'); // Obtém o valor do atributo alt como zona
        filterZone(zone);
    });
});

// Função para filtrar os dados no ViewModel
window.filterZone = function (zone) {
    console.log('Filtering data for zone:', zone);

    if (!vmInstance) {
        console.error('vmInstance não está definido!');
        return;
    }

    // Filtra os registros com base na zona
    var filteredRecords = vmInstance.allRecords().filter(record => record.City === zone);

    // Atualiza os registros filtrados
    vmInstance.records(filteredRecords);

    console.log('Filtered records:', filteredRecords);
};

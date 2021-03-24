// Load the elements in the page
function loadElements(url, defaultImage) {
    let container = document.getElementById('main-container');
    // Limpiara el container
    cleanContainer(container);
    // Agregamos un loader mientras carga
    let div_loader = document.createElement('div');
    div_loader.innerHTML= '<div class="loader"></div>';
    container.appendChild(div_loader);
    
    fetch(url).then(response => response.json()).then(function(data){        
        
        // Limpiara del container el loader
        cleanContainer(container);
        // Preparamos los div contenedores
        let div_products = document.createElement('div');
        let div_pagination = document.createElement('div');
        div_products.classList.add('container');
        div_products.id = 'products-container';
        div_pagination.classList.add('container');
        div_pagination.id = 'pagination-container';
        container.appendChild(div_products);
        container.appendChild(div_pagination);   
        
        if (data['count'] > 0) {
            // Rellenamos con todos los productos
            fillProducts(data['results'], defaultImage);

            // Rellenamos la paginacion
            if (data['previous'] !== null) {
                let div_previous = document.createElement('div');
                div_previous.classList.add('element-pagination');
                div_previous.innerHTML=
                    '<a href="javascript:loadElements(\'' + data['previous'] + '\', \'' 
                    + defaultImage + '\');"><i class="fa fa-hand-o-left"></i></a>';
                div_pagination.appendChild(div_previous); 
            }
            if (data['next'] !== null) {
                let div_next = document.createElement('div');
                div_next.classList.add('element-pagination');
                div_next.innerHTML=
                    '<a href="javascript:loadElements(\'' + data['next'] + '\', \'' 
                    + defaultImage + '\');"><i class="fa fa-hand-o-right"></i></a>';
                div_pagination.appendChild(div_next); 
            }       
        } else {
            div_products.innerHTML = 
                '<div style="margin-left: 20px;">'+
                    '<h1>No se encontraron coincidencias</h1>'+
                '</div>';  
        } 
    })
}
// Clean the div container
function cleanContainer(div_container){
    while (div_container.hasChildNodes()){
        div_container.removeChild(div_container.firstChild)
    }
}
// Load the products in the div products-container
function fillProducts(products, defaultImage){
    for (let i = 0; i < products.length; i++) {

        let div_cont = document.getElementById('products-container');

        let div_element = document.createElement('div');
        div_element.classList.add('element');                       

        let div_price = document.createElement('div');
        div_price.classList.add('price');

        div_price.innerHTML = 
            "<p style='font-size: 25px;'>" + products[i]['price'] + "</p>" + 
            "<button><i class='fa fa-shopping-basket'></i></button>";
        
        let subdiv = document.createElement('div');

        let default_image = defaultImage;
        if (products[i]['url_image'] !== null) {
            default_image = products[i]['url_image']
        }

        subdiv.innerHTML = 
            "<p style='font-size: 18px;'>" + products[i]['name'] + "</p>" +
            "<img src='" + default_image + "' alt='' style='width:100%'>"
        
        div_element.appendChild(div_price);
        div_element.appendChild(subdiv);
        div_cont.appendChild(div_element);  
    }
}
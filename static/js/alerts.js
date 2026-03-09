const formCreate = document.getElementById('formCreate') 
const inputFile = document.getElementById('id_image')

formCreate.addEventListener('submit', function(event) {
    // 3. Prevenir que se recargue la página
    event.preventDefault();
    Swal.fire({
        title: "Quieres guardar los cambios?",
        showDenyButton: true,
        showCancelButton: true,
        confirmButtonText: "Guardar",
        denyButtonText: `No guardar`,
        icon: 'info'
    }).then((result) => {
        if (result.isConfirmed) {            
            formCreate.submit()
        } else if (result.isDenied) {
            inputFile.value = ''
            Swal.fire("Cambios no guardados", "", "info");
        }
    });
});
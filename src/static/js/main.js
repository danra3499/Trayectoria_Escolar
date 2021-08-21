const btn_delete = document.querySelectorAll('.btn-delete')

if (btn_delete) {
  const btn_array = Array.from(btn_delete)
  btn_array.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      if (!confirm('Estas seguro de eliminar')) {
        e.preventDefault()
      }
    })
  })
}
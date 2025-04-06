document.getElementById('add_item').addEventListener('click', function () {
  const list = document.querySelector('.my_list')[0];
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  list.appendChild(newItem);
});

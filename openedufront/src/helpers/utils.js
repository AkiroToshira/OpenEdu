const month = ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень']
const url = "http://127.0.0.1:8000";
const checkIfUserLogged = () => !!JSON.parse(localStorage.getItem('user'));

export {
  month,
  url,
  checkIfUserLogged,
}
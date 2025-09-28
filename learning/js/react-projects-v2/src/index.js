
import ReactDOM from 'react-dom/client';
import ItemList from './components/ItemList';


function App() {
  return (
    <div>
      <h1>Cartoon characters</h1>
      <ItemList />
    </div>
  )
}

const container = document.getElementById('root');
const root = ReactDOM.createRoot(container);

root.render(<App />);

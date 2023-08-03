import './App.css';
import { BrowserRouter,Routes, Route } from 'react-router-dom';
import Tasks from './components/Tasks';
import ViewCard from './components/ViewCard';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Tasks/>} />
          <Route path="/viewcard" element={<ViewCard/>} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;

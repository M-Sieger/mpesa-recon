import './index.css';

import Header from './components/Header';
import UploadAndPreview from './components/UploadAndPreview';

function App() {
  return (
    <div className="app-wrapper">
      <Header />
      <main className="main-content">
        <UploadAndPreview />
      </main>
    </div>
  );
}

export default App;

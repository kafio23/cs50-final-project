import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/data')
      .then(res => {
        setData(res.data.data);
      })
  }, []);

  return (
    <div className='container text-center'>
      <div className='mt-4 mb-2'>
        <br></br>
        <h1>Welcome to Emotify!</h1>
      </div>
      <div className='form-container mt-4'>
        <div className='form-div'>
          <form className='row mt-3' action='http://127.0.0.1:5000/' method='post'>
            <div className='mb-3'>
              <label className='form-label main-label'>Share how you feel today!</label>
              <div className='textarea-div'>
                <textarea className='form-control mt-2' id='textareaResponseId' name='textareaResponse' rows='3' required='required'></textarea>
              </div>
            </div>
            <div className='col'>
              <button type="submit" className='btn btn-lg mb-3'>Submit</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default App;
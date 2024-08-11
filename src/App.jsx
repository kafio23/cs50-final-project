import React, { useState } from 'react';
import axios from 'axios';
import WebPlayback from './Webplayback';
import Auth from './Auth';

const App = () => {
  const accessToken = Auth()
  const [showSpinner, setShowSpinner] = useState(false)
  const [data, setData] = useState({})
  const [showPlayer, setShowPlayer] = useState(false)
  const [isButtonDisabled, setButtonDisabled] = useState(false)
  const [textareaResponse, setTextareaResponse] = useState('')
  const [imageUrl, setImageUrl] = useState('')
  const [trackUri, setTrackUri] = useState()


  const handleTextareaChange = (event) => {
    setTextareaResponse(event.target.value);
  };

  const disableButton = () => {
    setButtonDisabled(true);
  };

  const updateImageUrl = (data) => {
    setImageUrl(data.album.images[0]?.url)
  }

  const setPlayingTrack = (data) => {
    setTrackUri(data?.uri)
    setShowSpinner(false)
  }

  const submit = () => {
    disableButton()
    setShowSpinner(true)

    axios.post('http://127.0.0.1:5000/emotify', { textareaResponse: textareaResponse })
      .then(res => {
        setData(res.data.data);
        setPlayingTrack(res.data.data);
        updateImageUrl(res.data.data);
      })
      .catch(error => {
        console.error('Axios Error:', error);
      });

    setShowPlayer(true)
  };

  return (
    <div className='container text-center'>
      <div className='mt-4 mb-2'>
        <br></br>
        <h1>Welcome to Emotify!</h1>
      </div>
      <div className='form-container mt-4'>
        <div className='spotify-div' hidden={!imageUrl}>
          <img src={imageUrl} alt='Logo' />
        </div>

        <div hidden={!showPlayer}>
          <WebPlayback accessToken={accessToken} trackUri={trackUri} />
        </div>

        <div className='form-div'>
          <form className='row mt-3'>
            <div className='spinner-div mt-3 mb-4' hidden={!showSpinner}>
              <div className='spinner-grow' style={{ marginRight: '7px' }} role='status'>
                <span className='visually-hidden'>Loading...</span>
              </div>
              <div className='spinner-grow' role='status'>
                <span className='visually-hidden'>Loading...</span>
              </div>
              <div className='spinner-grow' style={{ marginLeft: '7px' }} role='status'>
                <span className='visually-hidden'>Loading...</span>
              </div>
            </div>
            <div className='mb-3' hidden={isButtonDisabled}>
              <label className='form-label main-label'>Share how you feel today!</label>
              <div className='textarea-div'>
                <textarea
                  className='form-control mt-2'
                  id='textareaResponseId'
                  name='textareaResponse'
                  rows='3'
                  required='required'
                  onChange={handleTextareaChange}
                ></textarea>
              </div>
            </div>
            <div className='col'>
              <button
                onClick={submit}
                className='btn btn-lg mb-3'
                disabled={isButtonDisabled}
                hidden={isButtonDisabled}
              >Submit</button>
            </div>
          </form>
        </div>
      </div>
    </div >
  );
};

export default App;
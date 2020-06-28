import React from 'react'

class CvWorkerMain extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      user: '',
      apiBaseUrl: 'localhost:8000/api/v1',

    }
  }

  render() {
    return (
      <div
        id='cv_worker_top'
        className='container'
      >
        <h5>
          Hey it's the app
        </h5>
      </div>
    )
  }

}

export default CvWorkerMain

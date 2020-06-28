import React from 'react'

class DashboardPanel extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      message: 'haha',
    }
  }

  render() {
    return (
      <div
        id='dashboard_panel_main'
        className='row'
      >
        the dashboard panel
        <div>
          tasks
        </div>
        <div>
          operations
        </div>
      </div>
    )
  }

}

export default DashboardPanel

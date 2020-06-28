import React from 'react'

class SettingsPanel extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      message: 'fafa',
    }
  }

  render() {
    return (
      <div
        id='settings_panel_main'
        className='row'
      >
        the settings panel
      </div>
    )
  }

}

export default SettingsPanel

import React from 'react'

class ConfigPanel extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      message: 'haha',
    }
  }

  render() {
    return (
      <div
        id='config_panel_main'
        className='row'
      >
        the config panel
      </div>
    )
  }

}

export default ConfigPanel

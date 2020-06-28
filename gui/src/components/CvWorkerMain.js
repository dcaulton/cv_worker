import React from 'react'
import {
  BrowserRouter as Router, 
  Switch,
  Route, 
  Link
} from 'react-router-dom'
import DashboardPanel from './DashboardPanel'
import SettingsPanel from './SettingsPanel'
import ConfigPanel from './ConfigPanel'

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
        <Router>
          <nav>
            <ul>
              <li>
                <Link to='/settings'>Settings</Link>
              </li>
              <li>
                <Link to='/config'>Config Wizard</Link>
              </li>
              <li>
                <Link to='/'>Dashboard</Link>
              </li>
            </ul>
          </nav>

          <Switch>
            <Route path='/settings'>
             <SettingsPanel />
            </Route>
            <Route path='/config'>
             <ConfigPanel />
            </Route>
            <Route path='/'>
             <DashboardPanel />
            </Route>
          </Switch>
        </Router>
      </div>
    )
  }

}

export default CvWorkerMain

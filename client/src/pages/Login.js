import React from 'react';
import {ReactComponent as Logo} from '../logo.svg';
class Login extends React.Component {
    state = {
      email: '',
      password: ''
    }

    handleChange = (e) => {
      const {name, value} = e.target;
      this.setState({[name]: value})
    }

    handleSubmit = (e) => {

    }
    render() {
      return (
        <div>
          <div>
              <Logo />
                </div>
                <div>
                    <form onSubmit={this.handleSubmit}>
          <input type='matricula' name='matricula' placeholder='matricula' required onChange={this.handleChange} />
          <input type='password' name='password' placeholder='contraseña' required onChange={this.handleChange} />
                        <button onSubmit={this.handleSubmit}> PROCEDER </button>
                    </form>
                </div>
        </div>
      );
    }
}


export default Login;

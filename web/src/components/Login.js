import styled from 'styled-components';
import {API_HOST} from "../helpers/constants";

const axios = require('axios');

const Container = styled.div`
  display: flex;
  padding: 64px 0;
  justify-content: center;
  align-items: center;
  flex-direction: column;
`

const LoginButton = styled.button`
  margin-top: 32px;
  background-color: #f66e46;
  color: white;
  font-size: 16px;
  padding: 8px 16px;
  border-radius: 8px;
  outline: none;
  cursor: pointer;
  border: 0;
`

function Login({ scopes }) {
  
  const onLogin = async () => {
    const url = `${API_HOST}/auth/login`
    const redirectPage = window.location.href.split('?')[0]
    const response = await axios.post(url, { redirect_page: redirectPage, scope: scopes })
    window.location = response.data.authorization_url
  };

  return (
    <Container>
      <div>You are not logged in. Click on Login Button</div>

      <LoginButton onClick={onLogin}>
        Login
      </LoginButton>
    </Container>
  )
}

export default Login

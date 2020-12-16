import React from 'react';
import styled from 'styled-components';

const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
`

const Box = styled.div`
  padding: 12px 24px;
  border-radius: 8px;
  background-color: #f33c3c;
  color: white;
  text-align: center;
`

function ErrorMessage({ message }) {
  if (!message) {
    return null;
  }
  
  return (
    <Container>
      <Box>
        { message }
      </Box>
    </Container>
  )
}

export default ErrorMessage

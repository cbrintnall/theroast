import React from "react";
import { Grid, Row, Col, Button } from 'react-bootstrap';
import './css/header.css';

class Header extends React.Component {
    render() {
        return (
            <Grid className="headerBody">
                <Row>
                    <Col className="headerCol">
                        <h1> The Roast </h1>
                    </Col>
                </Row>
                <hr />
                <Row>
                    <Col className="headerCol">
                        <Button 
                            className="loginButton"
                            bsSize="large"> Signup </Button>
                        <Button 
                            className="loginButton"
                            bsSize="large"> Login </Button>
                    </Col>
                </Row>
            </Grid>
        )
    }
}

export default Header;
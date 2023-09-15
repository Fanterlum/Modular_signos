//import React from 'react';
//import { View } from 'react-native';
//import Login from './Login.js';

//const App = () => {
//  return (
//    <Login/>
//  );
//};

//export default App;

import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import 'react-native-gesture-handler';
import Login from './Login.js';
import Registro from './Registro.js';
import Home from './src/screens/Home.js'; //HOME.JS HACE LA CONEXIÓN DEL MENÚ DESPLEGABLE


const Stack = createStackNavigator();

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen name="Login" component={Login} options={{ headerShown: false }} />
        <Stack.Screen name="Home" component={Home} options={{ headerShown: true }}/>
        <Stack.Screen name="Registro" component={Registro} options={{ headerShown: false }}/>
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
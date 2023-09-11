// Navigation.js
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { View, Text, Button } from 'react-native';


//Screens used in the navigation
import Alert_Settings from "../screens/Alert_Settings";
import Patient_Info from "../screens/Patient_Info";
const Drawer = createDrawerNavigator();

const Navigation = () => {
  return (
    <NavigationContainer>
      <Drawer.Navigator initialRouteName="Paciente" screenOptions={{
        headerTitle: '',
        headerStyle: {
          backgroundColor: '#45C3CC', // Cambiar el color de fondo del encabezado
        },
      }}>
        <Drawer.Screen name="Paciente" component={Patient_Info} />
        <Drawer.Screen name="Alertas" component={Alert_Settings} />
      </Drawer.Navigator>
    </NavigationContainer>
  );
};

export default Navigation;

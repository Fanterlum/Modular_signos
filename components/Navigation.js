// Navigation.js
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { View, Text, Button } from 'react-native';
import CustomDrawer from './CustomDrawer';
import Icon from 'react-native-vector-icons/Ionicons';
//Screens used in the navigation
import Dashboard from "../screens/Dashboard";
import Patient_Info from "../screens/Patient_Info";
import Doctor_Info from '../screens/Doctor_Info';
import Paciente_List from '../screens/Patient_List';
import Statistics from '../screens/Statistics';
import Medical_History from '../screens/Medical_History';
import Patient_ID_info from '../screens/Patient_ID_info';
const Drawer = createDrawerNavigator();

const Navigation = () => {
  return (
    <>
      <Drawer.Navigator drawerContent= {props=> <CustomDrawer {...props}/>} initialRouteName="Dashboard" screenOptions={{
        headerTitle: '',
        backgroundColor: "#45C3CC",
        drawerActiveBackgroundColor: "#45C3CC",
        drawerActiveTintColor: "#fff",
        drawerInactiveTintColor: "#333",
        drawerStyle: {
          backgroundColor: '#FFFF',
        },
        drawerLabelStyle:{
          fontWeight: "bold",
          fontSize: 18,
        },
        headerStyle: {
          backgroundColor: '#45C3CC', // Cambiar el color de fondo del encabezado
        },
      }}
      >
        <Drawer.Screen name="Dashboard" component={Dashboard} options={{
          drawerIcon: (color) => (
            <Icon name='home-outline' size={26} color ={color}></Icon>
          )
        }
        }/>
        <Drawer.Screen name="Paciente" component={Patient_Info} options={{
          drawerIcon: (color) => (
            <Icon name='person-outline' size={26} color ={"black"}></Icon>
          )
        }
        }/>
        <Drawer.Screen name="Doctor" component={Doctor_Info} options={{
          drawerIcon: (color) => (
            <Icon name='medical-outline' size={26} color ={color}></Icon>
          ),
        }
        }/>
        <Drawer.Screen name="Lista de pacientes" component={Paciente_List} options={{
          drawerIcon: (color) => (
            <Icon name='list-outline' size={26} color ={color}></Icon>
          ),
        }
        }/>
        <Drawer.Screen name="Estadistica" component={Statistics} options={{
    drawerItemStyle: { height: 0 }
      }}/>
        <Drawer.Screen name="History" component={Medical_History} options={{
    drawerItemStyle: { height: 0 }
      }}/>
        <Drawer.Screen name="IdPaciente" component={Patient_ID_info} options={{
          drawerItemStyle: { height: 0 }
        }
        }/>
      </Drawer.Navigator>
    </>
  );
};

export default Navigation;

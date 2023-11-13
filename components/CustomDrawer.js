import { View, Text, StyleSheet, ImageBackground, Image, PixelRatio } from 'react-native'
import React from 'react'
import { DrawerContentScrollView, DrawerItemList } from '@react-navigation/drawer'
import Icon from 'react-native-vector-icons/Ionicons';
import { TouchableOpacity } from 'react-native-gesture-handler';
//Sesion del usuario
import { useUser } from './Context/UserProvider';
import { useEmail } from './Context/EmailProvider';
import { useJson } from './Context/JsonProvider';
/*
    Se requiere obtener de la base de datos la foto de perfil del usuario
    Su usuario y apellidos para mostrarse en la navegacion
    Y utilizar su id en las diferentes vistas
*/
const CustomDrawer = (props) => {
  const { userID, clearUserID } = useUser();
  const {Email, clearEmail} = useEmail();
  const {Json, clearJson } = useJson();
  const { navigation } = props;
  const DrawerPhoto = "../assets/drawerWallpaper.png";
  const imageUrl = require('../assets/Sample/Patient.jpeg');
  const UserName = "Vicente Gonzalez Garcia";

  //Cerrar sesión
  const handleLogout = () => {
    navigation.navigate('Login');
    clearUserID();
    clearEmail();
    clearJson();
  };
  //Tamaño responsivo para el fondo y la foto de perfil
  const fondoHeightResponsive = PixelRatio.getPixelSizeForLayoutSize(50);
  const fondoWidthResponsive = PixelRatio.getPixelSizeForLayoutSize(110);

  const fotoHeightResponsive = PixelRatio.getPixelSizeForLayoutSize(25);
  const fotoWidthResponsive = PixelRatio.getPixelSizeForLayoutSize(25);

  return (
    <View style={{flex:1}}>
        <DrawerContentScrollView
            {...props}
            contentContainerStyle= {{backgroundColor: "#45C3CC"}}>
        <ImageBackground
        source={require(DrawerPhoto)}
        style={{padding: 30, height: fondoHeightResponsive, width: fondoWidthResponsive}}>
            <Image
            source={imageUrl}
            style={[styles.userPhoto,{height: fotoHeightResponsive, width: fotoWidthResponsive}]}
            ></Image>
            <Text style={styles.textName}>{UserName}</Text>
        </ImageBackground>
        <View style={styles.lista}>
            <DrawerItemList {...props} />
        </View>
        </DrawerContentScrollView>
        <TouchableOpacity onPress={handleLogout}>
            <View style={styles.logout}>
            <Icon name='log-out-outline' size={28} color ={"black"}></Icon>
            <Text style={styles.textLogout}>Cerrar Sesión</Text>
            </View>
        </TouchableOpacity>
    </View>
  )
}

export default CustomDrawer
const styles = StyleSheet.create({
    textLogout:{
        marginLeft: "5%",
        marginTop: "1%",
        fontWeight: "bold",
        fontSize: 18,
    },
    logout:{
        padding: "10%",
        paddingTop: "5%",
        flexDirection: "row",
    },
    lista:{
        flex: 1,
        backgroundColor: "#fff"
    },
    userPhoto: {
        borderRadius: 40,
        marginLeft: "-2%",
        marginTop: "-3%",
    },
    textName: {
        position: "absolute",
        color: "#fff",
        fontSize: 16,
        fontWeight: "bold",
        left: "15%",
        top: "125%",
    },
});

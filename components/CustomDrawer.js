import { View, Text, StyleSheet, ImageBackground, Image } from 'react-native'
import React from 'react'
import { DrawerContentScrollView, DrawerItemList } from '@react-navigation/drawer'
import Icon from 'react-native-vector-icons/Ionicons';
import { TouchableOpacity } from 'react-native-gesture-handler';

const CustomDrawer = (props) => {
  const { navigation } = props;
  const DrawerPhoto = "../assets/drawerWallpaper.png";
  const imageUrl = require('../assets/Sample/Patient.jpeg');
  const UserName = "Vicente Gonzalez Garcia";

  //Cerrar sesión
  const handleLogout = () => {
    navigation.navigate('Login');
  };
  return (
    <View style={{flex:1}}>
        <DrawerContentScrollView
            {...props}
            contentContainerStyle= {{backgroundColor: "#45C3CC"}}>
        <ImageBackground
        source={require(DrawerPhoto)}
        style={{padding: 30}}>
            <Image
            source={imageUrl}
            style={styles.userPhoto}
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
        height: 80,
        width: 80,
        borderRadius: 40,
    },
    textName: {
        color: "#fff",
        fontSize: 16,
        fontWeight: "bold",
        marginTop: "2%",
    },
});

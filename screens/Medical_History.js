import React, { useState, useEffect } from 'react';
import { View, StyleSheet, ActivityIndicator, ScrollView } from 'react-native';
import Svg, { Line, Circle, Rect, Text } from 'react-native-svg';
import { Text as RNText } from 'react-native';
import GetGraph from '../backend/GetGraph';
import GetPromGraph from '../backend/GetPromGraph';
import { useFocusEffect } from '@react-navigation/native';

const MedicalHistoryGraph = ({ SignalData }) => {
  const graphWidth = SignalData.PUNTO_FINAL_X + 10;
  const graphHeight = 380;
  const backgroundColor = 'white';
  const gridLineColor = 'red';
  const gridSize = 20;

  const generateGridLines = () => {
    const lines = [];

    for (let y = gridSize; y < graphHeight; y += gridSize) {
      lines.push(
        <Line key={`h${y}`} x1="0" y1={y} x2={graphWidth} y2={y} stroke={gridLineColor} strokeWidth="1" strokeOpacity="0.5" />
      );
    }

    for (let x = gridSize; x < graphWidth; x += gridSize) {
      lines.push(
        <Line key={`v${x}`} x1={x} y1="0" x2={x} y2={graphHeight} stroke={gridLineColor} strokeWidth="1" strokeOpacity="0.5" />
      );
    }

    return lines;
  };

  return (
    <View>
      <Svg width={graphWidth} height={graphHeight}>
        <Rect x="0" y="0" width={graphWidth} height={graphHeight} fill={backgroundColor} />
        {generateGridLines()}
        <Line x1={SignalData.PRIMER_PUNTO_X} y1={SignalData.PRIMER_PUNTO_Y} x2={SignalData.P_SIGNAL_X} y2={SignalData.P_SIGNAL_Y} stroke="black" strokeWidth="2" />
        <Line x1={SignalData.P_SIGNAL_X} y1={SignalData.P_SIGNAL_Y} x2={SignalData.Q_SIGNAL_X} y2={SignalData.Q_SIGNAL_Y} stroke="black" strokeWidth="2" />
        <Line x1={SignalData.Q_SIGNAL_X} y1={SignalData.Q_SIGNAL_Y} x2={SignalData.PUNTO_MAS_ALTO_X} y2={SignalData.PUNTO_MAS_ALTO_Y} stroke="black" strokeWidth="2" />
        <Line x1={SignalData.PUNTO_MAS_ALTO_X} y1={SignalData.PUNTO_MAS_ALTO_Y} x2={SignalData.S_SIGNAL_X} y2={SignalData.S_SIGNAL_Y} stroke="black" strokeWidth="2" />
        <Line x1={SignalData.S_SIGNAL_X} y1={SignalData.S_SIGNAL_Y} x2={SignalData.T_SIGNAL_X} y2={SignalData.T_SIGNAL_Y} stroke="black" strokeWidth="2" />
        <Line x1={SignalData.T_SIGNAL_X} y1={SignalData.T_SIGNAL_Y} x2={SignalData.PUNTO_FINAL_X} y2={SignalData.PUNTO_FINAL_Y} stroke="black" strokeWidth="2" />

        <Circle cx={SignalData.PRIMER_PUNTO_X} cy={SignalData.PRIMER_PUNTO_Y} r="4" fill="red" />
        <Circle cx={SignalData.PUNTO_MAS_ALTO_X} cy={SignalData.PUNTO_MAS_ALTO_Y} r="4" fill="red" />
        <Circle cx={SignalData.PUNTO_FINAL_X} cy={SignalData.PUNTO_FINAL_Y} r="4" fill="red" />
        <Circle cx={SignalData.Q_SIGNAL_X} cy={SignalData.Q_SIGNAL_Y} r="4" fill="red" />
        <Circle cx={SignalData.S_SIGNAL_X} cy={SignalData.S_SIGNAL_Y} r="4" fill="red" />
        <Circle cx={SignalData.T_SIGNAL_X} cy={SignalData.T_SIGNAL_Y} r="4" fill="red" />
        <Circle cx={SignalData.P_SIGNAL_X} cy={SignalData.P_SIGNAL_Y} r="4" fill="red" />
        <Text x={SignalData.PUNTO_MAS_ALTO_X + 1} y={SignalData.PUNTO_MAS_ALTO_Y - 5} fontSize="12" fontWeight="bold" fill="black">
          R
        </Text>
        <Text x={SignalData.Q_SIGNAL_X + 1} y={SignalData.Q_SIGNAL_Y + 13} fontSize="12" fontWeight="bold" fill="black">
          Q
        </Text>
        <Text x={SignalData.S_SIGNAL_X + 1} y={SignalData.S_SIGNAL_Y + 13} fontSize="12" fontWeight="bold" fill="black">
          S
        </Text>
        <Text x={SignalData.T_SIGNAL_X + 1} y={SignalData.T_SIGNAL_Y - 5} fontSize="12" fontWeight="bold" fill="black">
          T
        </Text>
        <Text x={SignalData.P_SIGNAL_X + 1} y={SignalData.P_SIGNAL_Y - 5} fontSize="12" fontWeight="bold" fill="black">
          P
        </Text>
      </Svg>
    </View>
  );
};

const Statistics = ({ route }) => {
  const userId = route.params?.userId;
  const [lastRecord, setLastRecord] = useState();
  const [weeklyAverage, setWeeklyAverage] = useState();
  const getRandomNumber = (min, max) => {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  };
  useFocusEffect(
    React.useCallback(() => {
      const randomData = {
        PRIMER_PUNTO_X: 0,
        PRIMER_PUNTO_Y: getRandomNumber(300, 331),
        PUNTO_MAS_ALTO_X: getRandomNumber(100, 120),
        PUNTO_MAS_ALTO_Y: getRandomNumber(30, 60),
        PUNTO_FINAL_X: getRandomNumber(255, 270),
        PUNTO_FINAL_Y: getRandomNumber(320, 350),
        Q_SIGNAL_X: getRandomNumber(90, 110),
        Q_SIGNAL_Y: getRandomNumber(330, 370),
        S_SIGNAL_X: getRandomNumber(130, 150),
        S_SIGNAL_Y: getRandomNumber(320, 360),
        T_SIGNAL_X: getRandomNumber(200, 215),
        T_SIGNAL_Y: getRandomNumber(260, 300),
        P_SIGNAL_X: getRandomNumber(40, 50),
        P_SIGNAL_Y: getRandomNumber(280, 290),
        OXIGENACION: getRandomNumber(80, 98),
        RITMOCARDIACO: getRandomNumber(60, 100),
        RESP: getRandomNumber(12, 24),
      };
      setLastRecord(randomData);
      const randomData2 = {
        PRIMER_PUNTO_X: 0,
        PRIMER_PUNTO_Y: getRandomNumber(300, 331),
        PUNTO_MAS_ALTO_X: getRandomNumber(100, 120),
        PUNTO_MAS_ALTO_Y: getRandomNumber(30, 60),
        PUNTO_FINAL_X: getRandomNumber(255, 270),
        PUNTO_FINAL_Y: getRandomNumber(320, 350),
        Q_SIGNAL_X: getRandomNumber(90, 110),
        Q_SIGNAL_Y: getRandomNumber(330, 370),
        S_SIGNAL_X: getRandomNumber(130, 150),
        S_SIGNAL_Y: getRandomNumber(320, 360),
        T_SIGNAL_X: getRandomNumber(200, 215),
        T_SIGNAL_Y: getRandomNumber(260, 300),
        P_SIGNAL_X: getRandomNumber(40, 50),
        P_SIGNAL_Y: getRandomNumber(280, 290),
        OXIGENACION: getRandomNumber(80, 98),
        RITMOCARDIACO: getRandomNumber(60, 100),
        RESP: getRandomNumber(12, 24),
      };
      setWeeklyAverage(randomData2);
    }, [])
  );

  console.log(lastRecord);
  console.log(weeklyAverage);

  return (
    <ScrollView style={styles.scrollView}>
      {/* Último registro */}
      <View style={styles.titlecontainer}>
        <RNText style={styles.title}>Historial semanal</RNText>
      </View>
      <View style={styles.container}>
        {lastRecord ? (
          <>
            <RNText style={styles.Textonormal}>Señal Actual</RNText>
            <MedicalHistoryGraph SignalData={lastRecord} />
            <RNText style={styles.Textonormal}>Oxigenacion: {lastRecord.OXIGENACION}</RNText>
            <RNText style={styles.Textonormal}>Ritmo cardiaco: {lastRecord.RITMOCARDIACO}</RNText>
            <RNText style={styles.Textonormal}>Frecuencia respiratoria: {lastRecord.RESP}</RNText>
          </>
        ) : (
          <ActivityIndicator />
        )}
      </View>

      {/* Promedio semanal */}
      <View style={styles.titlecontainer}>
        <RNText style={styles.title}>Promedio semanal</RNText>
      </View>
      <View style={styles.container}>
        {weeklyAverage ? (
          <>
            <MedicalHistoryGraph SignalData={weeklyAverage} />
            <RNText style={styles.Textonormal}>Oxigenacion: {weeklyAverage.OXIGENACION}</RNText>
            <RNText style={styles.Textonormal}>Ritmo cardiaco: {weeklyAverage.RITMOCARDIACO}</RNText>
            <RNText style={styles.Textonormal}>Frecuencia respiratoria: {weeklyAverage.RESP}</RNText>
          </>
        ) : (
          <ActivityIndicator />
        )}
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  scrollView: {
    flex: 1,
    backgroundColor: 'white',
  },
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    height: '75%',
    backgroundColor: 'white',
  },
  titlecontainer: {
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'white',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    marginTop: '5%',
  },
  Textonormal: {
    fontSize: 18,
    fontWeight: 'bold',
    marginTop: '2%',
  },
});

export default Statistics;

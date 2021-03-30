export interface NationalSummaryModel {
  lastUpdate: string;
  italia: {
    tiPercentage: number;
    tiIncrement: number;
    newPositives: number;
    newPositivesIncrement: number;
    weeklyPositives: number;
    weeklyPositivesIncrement: number;
  },
  toscana: {
    tiPercentage: number;
    tiIncrement: number;
    newPositives: number;
    newPositivesIncrement: number;
    weeklyPositives: number;
    weeklyPositivesIncrement: number;
  };
  veneto: {
    tiPercentage: number;
    tiIncrement: number;
    newPositives: number;
    newPositivesIncrement: number;
    weeklyPositives: number;
    weeklyPositivesIncrement: number;
  };
  marche: {
    tiPercentage: number;
    tiIncrement: number;
    newPositives: number;
    newPositivesIncrement: number;
    weeklyPositives: number;
    weeklyPositivesIncrement: number;
  };
}

export interface VaccinesSummaryModel {
  lastUpdate: string;
  italy: {
    fullVaccPopulation: number;
    dailyShots: number;
    dailyShotsIncrement: number;
    dailyFirstShots: number;
    dailyFirstShotsIncrement: number;
    dailySecondShots: number;
    dailySecondShotsIncrement: number;
  };
  toscana: {
    fullVaccPopulation: number;
    dailyShots: number;
    dailyShotsIncrement: number;
    dailyFirstShots: number;
    dailyFirstShotsIncrement: number;
    dailySecondShots: number;
    dailySecondShotsIncrement: number;
  };
  veneto: {
    fullVaccPopulation: number;
    dailyShots: number;
    dailyShotsIncrement: number;
    dailyFirstShots: number;
    dailyFirstShotsIncrement: number;
    dailySecondShots: number;
    dailySecondShotsIncrement: number;
  };
  marche: {
    fullVaccPopulation: number;
    dailyShots: number;
    dailyShotsIncrement: number;
    dailyFirstShots: number;
    dailyFirstShotsIncrement: number;
    dailySecondShots: number;
    dailySecondShotsIncrement: number;
  };
}

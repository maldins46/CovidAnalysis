export interface AppbarAction {
  id: string;
  name: string;
  execute: (() => void);
  mdiIcon: string;
  disabled?: boolean;
}

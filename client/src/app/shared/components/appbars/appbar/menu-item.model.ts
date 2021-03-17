export interface MenuItem {
  name: string;
  mdiIcon: string;
  tooltip: string;
  route: string;
  extendedText: boolean;
}

export class MenuItemsUtils {
  /**
   * Set Home item as the first item, leave the others untouched.
   * @param items Menu items.
   */
  static sortItems(items: MenuItem[]): MenuItem[] {
    return items.sort(
      (a) => (a.name === 'Home') ? -1 : 0
    );
  }
}

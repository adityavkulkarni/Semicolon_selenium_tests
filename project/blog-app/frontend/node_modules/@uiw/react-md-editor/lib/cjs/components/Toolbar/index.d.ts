import { Component } from 'react';
import { IProps } from '../../utils';
import { ICommand } from '../../commands';
import './index.less';
export interface IToolbarProps extends IProps {
    onCommand?: (command: ICommand) => void;
    commands: ICommand[];
    active?: {
        [key: string]: any;
    };
}
export default class Toolbar extends Component<IToolbarProps> {
    static defaultProps: IToolbarProps;
    handleClick: (command: ICommand) => void;
    render(): JSX.Element;
}

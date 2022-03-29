import React from 'react';
import { SvgIcon, SvgIconProps } from '@material-ui/core';
import { ReactComponent as StakeIcon } from './images/stake.svg';

export default function Stake(props: SvgIconProps) {
  return <SvgIcon component={StakeIcon} viewBox="0 0 34 34" {...props} />;
}
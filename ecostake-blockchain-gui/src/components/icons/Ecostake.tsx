import React from 'react';
import { SvgIcon, SvgIconProps } from '@material-ui/core';
import { ReactComponent as EcostakeIcon } from './images/ecostake.svg';

export default function Keys(props: SvgIconProps) {
  return <SvgIcon component={EcostakeIcon} viewBox="0 0 58 58" {...props} />;
}

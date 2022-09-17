import * as Rect from 'react';
import WalletConnectProvider from '@walletconnect/react-native-dapp';
import AsyncStorage from '@react-native-async-storage/async-storage';

export default function App(): JSX.Element {
  return (
    <WalletConnectProvider
      redirectUrl={Platform.OS === 'web' ? window.location.origin : '3rbble://'}
      storageOptions= {{
        asyncStorage: AsyncStorage,
      }}>
      <>{'3rbble'}</>
    </WalletConnectProvider>
  );
}
